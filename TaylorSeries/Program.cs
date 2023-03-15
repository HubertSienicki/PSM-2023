namespace TaylorSeries;

public static class Program
{
    static void Main(string[] args)
    {
        const double x = 1;
        var sinX = Sin(x);
        var mathSinX = Math.Sin((Math.PI * x) / 180);
        var diff = Math.Abs(sinX - mathSinX);
        Console.WriteLine($"sin({x}) = {sinX}");
        Console.WriteLine($"Math.sin({x}) = {mathSinX}");
        Console.WriteLine($"Difference: {diff}");
    }

    private static double Sin(double x)
    {
        x = x % (2 * Math.PI); // sprowadzenie kąta do przedziału [0, 2π]
        x = (Math.PI * x) / 180;
        var result = 0.0;
        var term = x;
        var sign = 1;
        for (var i = 1; i <= 10; i++)
        {
            result += sign * term;
            term *= -x * x / ((2 * i) * (2 * i + 1));
            sign *= -1;
        }
        return result;
    }
}