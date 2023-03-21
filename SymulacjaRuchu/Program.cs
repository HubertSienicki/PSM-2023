namespace SymulacjaRuchu;

public static class Program
{
    private static void Main(string[] args)
    {
        // definicja zmiennych i stałych
        double x = 0, y = 0; // pozycja
        double vx = 10, vy = 20; // prędkość
        double ax = 0, ay = 0; // przyspieszenie
        double m = 1; // masa
        var q = 0.5; // współczynnik oporu ośrodka
        var dt = 0.01; // krok czasowy
        double t = 0; // czas

        // symulacja
        while (t < 10)
        {
            // obliczenie siły grawitacji
            var g = 9.81; // przyspieszenie ziemskie
            double Fg_x = 0; // siła grawitacji w kierunku X
            var Fg_y = -m * g; // siła grawitacji w kierunku Y

            // obliczenie siły oporu ośrodka
            var V = Math.Sqrt(vx * vx + vy * vy); // prędkość względem ośrodka
            var Fo_x = -q * V * vx; // siła oporu ośrodka w kierunku X
            var Fo_y = -q * V * vy; // siła oporu ośrodka w kierunku Y

            // obliczenie wypadkowej siły
            var Fx = Fg_x + Fo_x; // siła wypadkowa w kierunku X
            var Fy = Fg_y + Fo_y; // siła wypadkowa w kierunku Y

            // obliczenie przyspieszenia
            ax = Fx / m; // przyspieszenie w kierunku X
            ay = Fy / m; // przyspieszenie w kierunku Y

            // obliczenie nowych prędkości i pozycji
            vx += ax * dt; // nowa prędkość w kierunku X
            vy += ay * dt; // nowa prędkość w kierunku Y
            x += vx * dt; // nowa pozycja w kierunku X
            y += vy * dt; // nowa pozycja w kierunku Y

            // wypisanie wyniku
            Console.WriteLine("t = {0:F2}, x = {1:F2}, y = {2:F2}", t, x, y);

            // zwiększenie czasu
            t += dt;
        }

        Console.ReadKey();
    }
}