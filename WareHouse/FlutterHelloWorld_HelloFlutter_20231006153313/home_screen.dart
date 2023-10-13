'''
import 'package:flutter/material.dart';
class HomeScreen extends StatelessWidget {
  final String greeting;
  HomeScreen({this.greeting});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('HelloWork'),
      ),
      body: Center(
        child: Text(
          greeting,
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}
'''