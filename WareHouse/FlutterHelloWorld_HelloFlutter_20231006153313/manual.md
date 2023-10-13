# HelloWork Mobile App User Manual

## Introduction

The HelloWork mobile app is a Flutter-based application that allows users to display a greeting message on their screen. This user manual will guide you through the installation process and explain how to use the app effectively.

## Installation

To install the HelloWork mobile app, follow these steps:

1. Make sure you have Flutter installed on your machine. If not, refer to the official Flutter documentation for installation instructions.

2. Clone the HelloWork repository from GitHub using the following command:

   ```
   git clone https://github.com/your-username/hello_work_app.git
   ```

3. Navigate to the project directory:

   ```
   cd hello_work_app
   ```

4. Install the required dependencies by running the following command:

   ```
   flutter pub get
   ```

5. Connect your mobile device or start an emulator.

6. Run the app using the following command:

   ```
   flutter run
   ```

   This will launch the HelloWork app on your device or emulator.

## Using the App

Once the HelloWork app is installed and running, follow these steps to use it:

1. The app will open with a screen displaying the greeting message "Hello, World!".

2. You can customize the greeting message by modifying the `greeting` parameter in the `HomeScreen` widget. Open the `home_screen.dart` file and locate the following line:

   ```dart
   HomeScreen({this.greeting});
   ```

   Change the value of `this.greeting` to your desired greeting message.

3. Save the changes and hot reload the app by pressing "r" in the terminal where the app is running. The greeting message will be updated accordingly.

4. To exit the app, press the back button on your device or close the emulator.

## Conclusion

Congratulations! You have successfully installed and used the HelloWork mobile app. Feel free to explore the code and make any modifications to suit your needs. If you have any questions or encounter any issues, please refer to the official Flutter documentation or seek assistance from the ChatDev support team. Enjoy using HelloWork!