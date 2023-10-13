'''
import 'package:flutter/material.dart';
import 'package:hello_work_app/home_screen.dart';
void main() {
  runApp(HelloWorkApp());
}
class HelloWorkApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'HelloWork',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomeScreen(greeting: 'Hello, World!'),
    );
  }
}
'''