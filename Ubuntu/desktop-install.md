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

## Starting the installation process
First, boot from the installation flash drive.
1. With the power off, insert the flash drive into the machine where you want to install Ubuntu.
2. Power up the computer and press whatever key is used to select the boot device (often it's F12.)
3. Select your flash drive from the menu of choices.

Next, select the Ubuntu image from the Ventoy menu.
1. Use arrow keys to scroll if needed.
2. Press Enter to boot.
3. Select Boot in normal mode.

Then, from the GNU GRUB menu, select Try or install Ubuntu.
1. Use arrow keys if needed.
2. Press Enter to confirm the selection.
3. Watch for the Ubuntu logo and spinning busy indicator.

## Ubuntu installation choices
You'll be asked to make a number of [choices during installation](https://linuxize.com/post/how-to-install-ubuntu-26-04/#boot-from-the-usb-drive). Most are self-explanatory. Those that are not are detailed below.
* When connecting to WiFi, you may not see your network. If this happens, press your keyboard's down arrow a few times until the list begins scrolling down.
* When asked what apps to start with, choose the default selection. Installation will be quicker and more apps can be installed later if needed.
* For proprietary software, the safe choice to ensure everything works is to say yes. If you know for certain your hardware is fully supported, you can leave it unselected.
* When asked how to install, choose _Erase disk and install Ubuntu_. You already backed up anything you wanted to keep, right?
* When asked where to install, the default choice is usually correct. If you see something like _nvme0n1_, that's your computer's solid state drive.
* For creating your account, you can either use your name or choose something generic, like Administrator and then setup your personal account later.

Once you click install, the process is automatic. You can kick back and relax. If you're installing onto a laptop, make sure it's plugged in.

When installation finishes and you reboot, you're ready to log in as the user you created and start customizing your system.

## Customizing the system
The first time you log into Ubuntu, you'll be shown a _getting started_ wizard. Most of the default selections are fine. Ubuntu leaves most of the intrusive and tracking features off unless you opt in. But, before you click Finish, select the Open App Center button.

Ubuntu has an [app store](https://linuxvox.com/blog/install-ubuntu-app-store/), just like Windows, Android, and iOS. You can use this to easily install applications you'll need. For a typical makerspace, the list below is a good start.

* Visual Studio Code for programming tasks (listed under Development.)
* LibreOffice for writing documentation (listed under Productivity.)

If you find yourself wanting additional apps later, you can find the App Center on the Ubuntu menu bar.

## Creating one or more non-privileged users
If you're sharing this computer with others, be sure to [create a user account](https://linux.how2shout.com/create-a-new-user-in-ubuntu-22-04-or-20-04-using-gui-or-terminal/) for each person. Alternatively, you can [create guest access](https://linuxconfig.org/how-to-enable-guest-session-on-ubuntu-20-04-focal-fossa-linux) that can be shared.

Interestingly enough, the Ubuntu user management tools do not allow you to assign users to groups, except by using command-line tools. If you find this to be inconvenient, you can run the following command in a terminal to install a GUI user and group management tool.

```
sudo apt install gnome-system-tools
```

Once installation is complete, there will be a new selection on the menu called Users and Groups.

## Keeping current with patches and updates
You should get in the habit of periodically [running the Update app](https://www.howtogeek.com/740795/how-to-update-ubuntu-linux/) from the program menu. This will keep your system secure and running smoothly.
