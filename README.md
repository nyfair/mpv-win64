# MPV Player Win64 Build

## Installation
Grab and extract the All-in-One archive from <https://github.com/nyfair/mpv-win64/releases>  
**Bleeding Edge** weekly build is based on the git trunk code of mpv and libplacebo. It includes the newest features and bug fixes but may be less stable  
**Latest** build is based on the stable releases of all libraries  
**x86-64-v3** build is optimized for CPUs that support the AVX2 instruction set, this includes most CPUs after 2013  
**x86-64-v4** build is optimized for CPUs that support the AVX512 instruction set, it is recommends for Intel CPUs after 2016  
**amd-zen4+** build is specifically optimized for AMD Zen4(7000 series) and newer CPUs  
You can also manually install these pacman-based packages if you are using MSYS2  
All my builds are portable and compiled with VapourSynth support, these plugins will have no effect if MPV can't find python environment

## Main project site:
<https://mpv.io/>

## Configuration
<https://mpv.io/manual/>  
All your configurations can be saved within the ***portable_config*** subdirectory

## Awesome Links
- [User Scripts from Official](https://github.com/mpv-player/mpv/wiki/User-Scripts)
- [Default MPV Setting](https://github.com/mpv-player/mpv/blob/master/etc/mpv.conf)
- [Default MPV Key Binding](https://github.com/mpv-player/mpv/blob/master/etc/input.conf)
### Lua Plugin
- [uosc](https://github.com/tomasklaen/uosc)
- [thumbfast](https://github.com/po5/thumbfast)
### VapourSynth Plugin
- [MVTools](https://github.com/dubhater/vapoursynth-mvtools) motion interpolation plugin and it was open source
- [FFMS2](https://github.com/FFMS/ffms2) video source library for multimedia editing
- [RIFE](https://github.com/HomeOfVapourSynthEvolution/VapourSynth-RIFE-ncnn-Vulkan) new motion interpolation based on rife-ncnn-vulkan
### Shader
- [Anime4K](https://bloc97.github.io/Anime4K/)
- [SSim/Krig](https://gist.github.com/igv)
- [FSRCNNX](https://github.com/igv/FSRCNN-TensorFlow/releases)
- [ACNet](https://github.com/TianZerL/ACNetGLSL/releases)

## How to Compile
Fork this repo and build these packages by Github Action  
**NOTICE**  
Don't build it on your personal msys2 environment unless it was in sandbox, these shitty scripts will spoil your whole weekend!

## Detail
The FFmpeg and MPV library were built with the following libraries
- lame: MP3 Audio Encoding
- libogg/libvorbis-aotuv: Ogg Vorbis Audio Encoding
- opus: Opus Audio Encoding
- nvcodec: Nvidia Hardware Accelerated video Encoding/Decoding
- lcms2: Reading ICC Profiles for Your Monitor
- libass/freetype2/fribidi/harfbuzz: Subtitle Support
- luajit: Lua Plugin
- vapoursynth: VapourSynth Plugin and VSS Video Source
- shaderc/spirv/libplacebo: D3D11 & Vulkan Context
- libbluray/libdvdnav/libdvdread/libdvdcss: Parsing BD/DVD
- libwebp: WebP Image Encoding/Decoding
- libjxl/highway/brotli: JPEG XL Image Encoding/Decoding

## TODO ???
### Build FFmpeg with x264/x265/rav1e/SVT-AV1/VVenC for video encoding
I prefer to directly use these utilities
### Build FFmpeg with libfdk_aac for high quality AAC audio encoding
Yes, Fraunhofer AAC produce better aac than FFmpeg native, but it is still not in the top tier. I recommend you to use xHE-AAC or Apple AAC instead
### Build libass with fontconfig for POSIX-like system font configuration
Fontconfig sucks on windows, and... do you really want to learn it?
### Build FFmpeg with dav1d for av1 decoding
~~Today all public av1 videos are just demos. I suggest you to try vvc for the purpose of testing~~  
ffmpeg has built-in av1 & vvc decoder now
