# MPV Player Win64 Build

## Installation
Grab and extract the All-in-One archive from <https://github.com/nyfair/mpv-win64/releases/tag/latest>  
You can also manually install these pacman-based package if you are using MSYS2  
All my builds are portable and compiled with VapourSynth support, these plugins will have no effect if MPV can't find python environment

## Main project site:
<https://mpv.io/>

## Configuration
<https://mpv.io/manual/>  
All your configuration can be saved within the ***portable_config*** subdirectory

## Useful Links
- [User Scripts from Official](https://github.com/mpv-player/mpv/wiki/User-Scripts)
- [Default MPV Setting](https://github.com/mpv-player/mpv/blob/master/etc/mpv.conf)
- [Default MPV Key Binding](https://github.com/mpv-player/mpv/blob/master/etc/input.conf)
### Lua Plugin
- [Autoload](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/autoload.lua)
- [Play List Manager](https://github.com/jonniek/mpv-playlistmanager)
- [MPV Thumbnail](https://github.com/TheAMM/mpv_thumbnail_script)
### VapourSynth Plugin
- [SVP](https://www.svp-team.com) proprietary motion interpolation solution to produce hight frame rate video
- [MVTools](https://github.com/dubhater/vapoursynth-mvtools) another motion interpolation plugin and it was open source
- [FFMS2](https://github.com/FFMS/ffms2) useful video source library for multimedia editing
### Shader
- [Anime4K](https://bloc97.github.io/Anime4K/)
- [SSim/Krig](https://gist.github.com/igv)
- [FSRCNNX](https://github.com/igv/FSRCNN-TensorFlow/releases)
- [ACNet](https://github.com/TianZerL/ACNetGLSL/releases)

## How to Compile
Forks this repo and build these library by Github Action  
**NOTICE**  
Don't build it on your personal msys2 environment unless it was in sandbox, these shitty script will spoil your whole weekend!

## Detail
The FFmpeg nad MPV library were build with the following library
- lame: MP3 Audio Encoding
- libogg/libvorbis-aotuv: Ogg Vorbis Audio Encoding
- opus: Opus Audio Encoding
- nvcodec: Nvidia Hardware Accelerated video Encoding/Decoding
- lcms2: Reading ICC Profiles for Your Monitor
- libass/freetype2/fribidi/harfbuzz: Subtitle Support
- luajit: Lua Plugin
- vapoursynth: VapourSynth Plugin and VSS Video Source

## TODO ???
### Build FFmpeg with x264/x265/libaom for video encoding
I prefer to directly use these utilities for better control
### Build FFmpeg with dav1d for software av1 decoding
AV1 is still not popular today, I suggest you to torture GPU instead of CPU
### Build FFmpeg with libfdk_aac for high quality AAC audio encoding
Yes, fdk aak produce better aac than FFmpeg native. But it is still not in the top tier. I recommend you to use xHE-AAC or Apple AAC instead
### Build MPV with fontconfig for POSIX-like system font configuration
Fontconfig sucks in windows, and... do you really want to learn it?
### Build MPV with SPIR-V and libplacebo for Vulkan context
This is meaningful, but currently d3d11 context also works