import json
from urllib import request
import in_place

resp = request.urlopen('https://github.com/nyfair/workflow/raw/master/old.json')
x = json.loads(resp.read().decode('utf-8'))
x = dict(map(lambda p: (p, x['data'][p]['version']), x['data'].keys()))
mingw = x['Mingw-w64'][:x['Mingw-w64'].find('ucrt')+4]
with in_place.InPlace('.github/workflows/toolchain.yml', newline='') as f:
  for l in f:
    if (i:=l.find('key: mcf_')) > -1:
      l = '%s%s\n' % (l[:i+9], mingw)
    elif (i:=l.find('curl')) > -1:
      l = '%s%s.7z --resolve "gcc-mcf.lhmouse.com:443:204.152.213.15"\n' % (l[:i+71], x['Mingw-w64'])
    f.write(l)
pkgs = {}
pkgs['mcfgthread'] = mingw[:8]
# pkgs['libvorbis_aotuv-dev'] = x['libvorbis']
pkgs['python-embed'] = x['Python']
pkgs['vapoursynth'] = x['VapourSynth'][1:]
pkgs['ffmpeg'] = x['ffmpeg']
pkgs['mpv'] = x['mpv']
for p in ['brotli', 'ffnvcodec', 'freetype2', 'fribidi', 'harfbuzz', 'highway', 'lame', 'lcms2', 'libass',
          'libbluray', 'libdvdcss', 'libdvdread', 'libdvdnav', 'libogg', 'libjxl', 'libplacebo',
          'libwebp', 'opus', 'shaderc', 'spirv-cross', 'vulkan']:
  pkgs['%s-dev' % p] = x[p]
for p in pkgs:
  with in_place.InPlace('%s/PKGBUILD' % p, newline='') as f:
    for l in f:
      if l.startswith('pkgver'):
        l = 'pkgver=%s\n' % pkgs[p]
      f.write(l)
pkgs['vapoursynth-dev'] = pkgs['vapoursynth']
pkgs['vapoursynth-plugin-core-extra'] = pkgs['vapoursynth']
pkgs['ffmpeg-dev'] = pkgs['ffmpeg']
for t in ['batch-stable.yml', 'batch-bleeding_edge-weekly.yml', 'ci.yml']:
  with in_place.InPlace('.github/workflows/%s' % t, newline='') as f:
    for l in f:
      if (i:=l.find('key: mcf_')) > -1:
        l = '%s%s\n' % (l[:i+9], mingw)
      elif (i:=l.find('/dev')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+15:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+15], p, pkgs[p], l[r:])
      elif (i:=l.find('/latest')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+18:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+18], p, pkgs[p], l[r:])
      f.write(l)

ffmpeg_git = pkgs['ffmpeg'].split('.')[:2]
mpv_git = pkgs['mpv'].split('.')[:2]
pkgs_git = {
  'ffmpeg': '%s.%dpre' % (ffmpeg_git[0], int(ffmpeg_git[1])+1),
  'mpv': '%s.%dpre' % (mpv_git[0], int(mpv_git[1])+1)
}
for p in pkgs_git:
  with in_place.InPlace('%s/PKGBUILD-git' % p, newline='') as f:
    for l in f:
      if l.startswith('pkgver'):
        l = 'pkgver=%s\n' % pkgs_git[p]
      f.write(l)
with in_place.InPlace('mpv/PKGBUILD-stablelib', newline='') as f:
  for l in f:
    if l.startswith('pkgver'):
      l = 'pkgver=%s\n' % pkgs_git['mpv']
    f.write(l)
with in_place.InPlace('.github/workflows/batch-bleeding_edge-weekly.yml', newline='') as f:
  for l in f:
    if (i:=l.find('/bleeding_edge')) > -1:
      r = l[i+25:]
      if r.startswith('ffmpeg-git-dev'):
        l = '%sffmpeg-git-dev-%s-1-x86_64.pkg.tar.zst\n' % (l[0:i+25], pkgs_git['ffmpeg'])
      elif r.startswith('ffmpeg-git'):
        l = '%sffmpeg-git-%s-1-x86_64.pkg.tar.xz\n' % (l[0:i+25], pkgs_git['ffmpeg'])
      elif r.startswith('mpv-git'):
        l = '%smpv-git-%s-1-x86_64.pkg.tar.xz\n' % (l[0:i+25], pkgs_git['mpv'])
    f.write(l)
