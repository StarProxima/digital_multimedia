import 'dart:math';

void main() {
  final random = Random();
  final img = List.generate(
      100, (_) => List.generate(100, (_) => random.nextDouble() * 255));

  final blur = gaussBlur(img, 7, 50);
  print(blur);
}

List<List<double>> gaussBlur(
    List<List<double>> img, int size, double deviation) {
  List<List<double>> kernel =
      List.generate(size, (_) => List.filled(size, 1.0));
  int a = (size + 1) ~/ 2;
  int b = (size + 1) ~/ 2;

  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      kernel[i][j] = gauss(i, j, deviation, a, b);
    }
  }

  double sum = 0;
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      sum += kernel[i][j];
    }
  }
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      kernel[i][j] /= sum;
    }
  }

  List<List<double>> blur =
      List.generate(img.length, (_) => List.filled(img[0].length, 0.0));
  int sx = size ~/ 2;
  int sy = size ~/ 2;

  for (int x = sx; x < img.length - sx; x++) {
    for (int y = sy; y < img[0].length - sy; y++) {
      double sum = 0;
      for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
          sum += img[x + i - sx][y + j - sy] * kernel[i][j];
        }
      }
      blur[x][y] = sum;
    }
  }

  return blur;
}

double gauss(int x, int y, double omega, int a, int b) {
  double omega2Pow2 = 2 * omega * omega;
  double m1 = 1 / (pi * omega2Pow2);
  double m2 = exp(-((pow(x - a, 2) + pow(y - b, 2)) / omega2Pow2));
  return m1 * m2;
}
