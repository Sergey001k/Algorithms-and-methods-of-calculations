#include <iostream>
#include <cmath>

double function(double x) {
	return 1 / (1 - 0.49 * pow(sin(x), 2));
}

//double function(double x) {
//	return cos(x) + 3;
//
//}

//double function(double x) {
//	return sqrt(9 - (x*x)) / (x*x);
//}

//double function(double x) {
//	return pow(cos(x), 3) * cos(3 * x);
//}


double sympson_calc(double(*f)(double), double a, double b, int n) {
	double h = (b - a) / n;
	double sum = f(a) + f(b);

	int k = 0;
	for (int i = 1; i < n; ++i) {
		k = 2 + 2 * (i % 2);
		sum += k * f(a + i * h);
	}
	sum *= h / 3;
	return sum;

}

int main() {
	setlocale(LC_ALL, "Russian");
	double a, b, n, Ih, Ih2, d = 1, eps = pow(10, -4);
	std::cout << "Границы отрезка a и b, количество отрезков n: " << std::endl;
	std::cin >> a >> b >> n;

	while (abs(d) >= eps) {
		Ih = sympson_calc(function, a, b, n);
		n *= 2;
		Ih2 = sympson_calc(function, a, b, n);
		d = (Ih - Ih2) / 15;
	}

	/*do {
		Ih = sympson_calc(function, a, b, n);
		n *= 2;
		Ih2 = sympson_calc(function, a, b, n);
		d = (Ih - Ih2) / 15;
	} while (abs(d) > eps);*/

	std::cout << "Значение интеграла: " << Ih2 + d << std::endl;
	std::cout << "Погрешность: " << abs(d) << std::endl;
	std::cout << "Значение n: " << n;

	return 0;
}