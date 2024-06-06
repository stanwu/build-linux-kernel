# build-kernel-bkqpb6

Ubuntu 20.04.6 LTS (GitHub Codespaces)

## How to Build the Kernel from Source Code Quickly

Fork this project and then open it with Codespaces. That's all.

## Linux Kernel

The Linux Kernel Long-Term Support (LTS) versions are crucial for maintaining the stability and security of various systems over extended periods. Here is a list of the currently supported LTS versions and their projected end-of-life (EOL) dates:

1. **Linux 6.1** - Supported until December 2026
2. **Linux 5.15** - Supported until December 2026
3. **Linux 5.10** - Supported until December 2026
4. **Linux 5.4** - Supported until December 2025
5. **Linux 4.19** - Supported until December 2024

Additionally, there are Super-Long-Term Support (SLTS) kernels, which extend support even further. The Linux 6.1 kernel, for instance, will enjoy support until August 2033 under the SLTS program.

For more details on the specific kernels and their updates, you can visit the [Linux Kernel Archives](https://www.kernel.org/category/releases.html).

## Android Kernel

The Android kernel Long-Term Supported (LTS) versions are maintained for an extended period to ensure stability, security, and long-term support for Android devices. These LTS kernels are derived from the upstream Linux LTS kernels with additional patches and modifications specific to Android. Here are the key Android LTS kernel versions:

1. **Android 5.15**
2. **Android 5.10**
3. **Android 5.4**
4. **Android 4.19**
5. **Android 4.14**
6. **Android 4.9**
7. **Android 4.4**

These kernels receive regular updates and backports of important fixes and security patches. Each of these LTS versions is supported for several years, ensuring that Android devices using these kernels remain secure and stable over time.

### Key Points about Android LTS Kernels:
- **Extended Support**: LTS kernels are maintained for a minimum of 2 years, often extending beyond that depending on community and vendor support.
- **Security and Stability**: Regular updates ensure that these kernels include the latest security patches and stability improvements.
- **Compatibility**: These kernels are designed to be compatible with various Android platform releases, allowing for device updates and long-term support.

For more detailed and up-to-date information about Android LTS kernels, you can refer to the [Android Kernel Overview](https://source.android.com/docs/core/architecture/kernel/kernel-overview)on the Android Open Source Project (AOSP) website.

## ChromeOS and ChromiumOS Kernel

The ChromeOS kernel versions used in Long-Term Support (LTS) releases are typically aligned with the Linux LTS kernels. As of the latest updates, the ChromeOS LTS channels provide more stable updates every six months to ensure security and feature stability. Here’s a summary of the current ChromeOS LTS versions and their corresponding Linux kernel versions:

1. **ChromeOS LTS 114** - This release is based on the Linux 5.10 LTS kernel. It is designed to offer stability and long-term support with updates focusing on security and critical bug fixes.

2. **ChromeOS LTS 102** - Previously based on the Linux 4.19 LTS kernel. This version ensures stability for devices that require extended support and less frequent updates.

3. **ChromeOS LTS 96** - Prior versions included older kernels like Linux 4.4 and 4.9, offering a solid foundation for earlier ChromeOS devices with extended support.

ChromeOS also employs a Long-Term Support Candidate (LTC) channel, which provides a preview of the next LTS version three months in advance, allowing administrators to test and prepare for upcoming updates.

For more detailed information on ChromeOS LTS versions and their release cycles, you can refer to the official [ChromeOS.dev long-term support releases](https://chromeos.dev/en) and the [Chrome Releases blog](https://chromereleases.googleblog.com/).

## Build Log:

- linux-6.9.3: test OK
- linux-6.1.92: test OK
- android14-6.1-2024-05_r5: test OK
- android13-5.15-2024-05_r2: test OK
- android-4.9: test OK
- chromiumos-6.1.92: test OK
- busybox-1.37.0.git: test OK 
- toybox-0.8.11-44-g2c3363f742eb: test OK

linux
```
./build.sh
```

android
```
./build-android-kernel.sh
```

or use `git tag` to list all of exist android kernel version

for example
```
git checkout android13-5.15-2024-05_r2
```

chromiumos
```
./build-chromiumos-kernel.sh
```
busybox
```
./build-busybox.sh
```

toybox
```
./build-toybox.sh
```
