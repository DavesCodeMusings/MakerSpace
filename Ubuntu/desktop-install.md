# Installing Ubuntu 26.4 LTS on Repurposed Hardware
This guide is for those interested in extending the life of older laptops and desktops. Maybe you have an old Windoze 10 machine that's out of support. Maybe you've upgraded to something new and are wondering what to do with the old machine. Whatever your reasons, this guide will help you get going.

The instructions here are intentionally brief. Use the links to external sources to get more detail on a particular task.

## Equipment needed
* Computer on which to install Ubuntu Linux.
* A second computer for downloading and preparing the Ubuntu installation flash drive.
* A USB flash drive large enough to hold the Ubuntu installation image (8G or larger.)

## Caution!
This installation will overwrite anything and everything on the target machine and the flash drive used for the installation. Be sure you have made copies of any files you want to keep!

## Preparing to install
In this guide, we'll use a DVD image for the installation, but we'll copy it onto a USB flash drive for speed and convenience. This will require a program (Ventoy) to manage images on the flash drive.

1. Install Ventoy on a flash drive. See the [Ventoy Getting Started](https://www.ventoy.net/en/doc_start.html) document to do this.
2. Download the latest Ubuntu Long Term Support (LTS) desktop image (currently 26.4 at time of writing.)
3. Copy the downloaded .ISO file to the Ventoy drive.
4. Eject the flash drive when the copy is finished.

## Installing
TODO

## Installing additional software
Ubuntu has an [app store](https://linuxvox.com/blog/install-ubuntu-app-store/), just like Windows, Android, and iOS. You can use this to easily install applications you'll need. For a typical makerspace, the list below is a good start.

* Visual Studio Code (for programming tasks.)
* LibreOffice (for writing documentation.)
* TODO

## Creating one or more non-privileged users
If you're sharing this computer with others, be sure to [create a user account](https://linux.how2shout.com/create-a-new-user-in-ubuntu-22-04-or-20-04-using-gui-or-terminal/) for each person. Alternatively, you can [create guest access](https://linuxconfig.org/how-to-enable-guest-session-on-ubuntu-20-04-focal-fossa-linux) that can be shared.

## Keeping current with patches and updates
You should get in the habit of periodically [running the Update app](https://www.howtogeek.com/740795/how-to-update-ubuntu-linux/) from the program menu. This will keep your system secure and running smoothly.
