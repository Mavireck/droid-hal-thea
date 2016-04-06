%define device thea
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty Moto G 2nd Gen LTE

%define android_config \
#define QCOM_BSP 1\
%{nil}

%define installable_zip 1

%define straggler_files \
/etc/fstab.qcom\
/init.mmi.boot.sh\
/init.mmi.touch.sh\
/init.qcom.ssr.sh\
/selinux_version\
/service_contexts\
%{nil}

%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}
%include rpm/dhd/droid-hal-device.inc
