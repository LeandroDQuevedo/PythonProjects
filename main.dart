// Imports the Flutter material package, which contains basic widgets.
import 'package:flutter/material.dart';

// The main entry point of your application.
void main() {
  runApp(const MyApp());
}

// The main application widget.
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      // The home page of the application.
      home: PhotoCleanerScreen(),
    );
  }
}

// The main screen where photos will be displayed and gestures will be detected.
class PhotoCleanerScreen extends StatefulWidget {
  const PhotoCleanerScreen({super.key});

  @override
  State<PhotoCleanerScreen> createState() => _PhotoCleanerScreenState();
}

class _PhotoCleanerScreenState extends State<PhotoCleanerScreen> {
  // A simple list of colors to simulate photos.
  final List<Color> _colors = [
    Colors.red,
    Colors.blue,
    Colors.green,
    Colors.yellow,
    Colors.purple,
  ];

  // Index of the current color (photo).
  int _currentIndex = 0;

  // Function to process the swipe gesture.
  void _handleSwipe(DragEndDetails details) {
    // The velocity of the drag on the X axis (horizontal).
    double velocityX = details.velocity.pixelsPerSecond.dx;

    // The velocity of the drag on the Y axis (vertical).
    double velocityY = details.velocity.pixelsPerSecond.dy;

    // Logic to determine the swipe direction.
    if (velocityX > 500) {
      // Swipe to the right.
      print('Swipe Right: Delete photo');
    } else if (velocityX < -500) {
      // Swipe to the left.
      print('Swipe Left: Keep photo');
    } else if (velocityY < -500) {
      // Swipe to the top.
      print('Swipe Up: Send to server');
    }

    // Advance to the next "photo" (color) in our example list.
    setState(() {
      _currentIndex = (_currentIndex + 1) % _colors.length;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Photo Cleaner'),
      ),
      body: Center(
        // The GestureDetector widget detects gestures.
        child: GestureDetector(
          // The onHorizontalDragEnd event is triggered when a horizontal drag ends.
          onHorizontalDragEnd: _handleSwipe,
          // The onVerticalDragEnd event is triggered when a vertical drag ends.
          onVerticalDragEnd: _handleSwipe,
          child: Container(
            width: 300,
            height: 400,
            color: _colors[_currentIndex],
            child: const Center(
              child: Text(
                'Swipe here!',
                style: TextStyle(fontSize: 24, color: Colors.white),
              ),
            ),
          ),
        ),
      ),
    );
  }
}