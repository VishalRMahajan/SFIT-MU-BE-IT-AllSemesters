import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MAD EXP 02',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
      ),
      home: MyHomePage(),
    ); //Material App
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('MAD EXP 02', style: TextStyle(color: Colors.white)),
        backgroundColor: Colors.deepPurpleAccent,
      ), // AppBar
      body: Center(
        child: Text(
          'Hello from Vishal Mahajan!',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
            color: Colors.deepPurpleAccent,
          ), //TextStyle
        ), //Text
      ), //Center
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: Icon(Icons.add, color: Colors.white),
        backgroundColor: Colors.deepPurpleAccent,
      ), //FloatingActionButton
      backgroundColor: Colors.white,
    ); //Scaffold
  }
}
