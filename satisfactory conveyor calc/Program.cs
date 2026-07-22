using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.Threading;
using System.Diagnostics;
using System.IO;

//this line contain 75 simbolssssssssssssssssssssssssssssssssssssssssssssss

public static class Program
{
    // находит НОД двух чисел по алгоритму евклида
    public static int gcd(int number1, int number2)
    {
        // тривиальный случай
        if (number1 == number2) { return number1; }

        // если условие не выполнится - тогда и только тогда
        // пойдёт остальная часть функции

        int first = Math.Min(number1, number2);
        int second = Math.Max(number1, number2);

        // алгоритм евклида
        while (first != second)
        {
            if (first > second) { first -= second; }
            else { second -= first; }
        }
        return first;
    }



    // находит НОК множества чисел
    public static int lcm(List<int> numbers)
    {
        int ansver;
        int g;

        ansver = numbers[0];

        for (int i = 1; i < numbers.Count(); i++)
        {
            g = gcd(ansver, numbers[i]);
            ansver *= numbers[i] / g;
        }

        return ansver;
    }



    // находит ближайшее большее число нормального вида
    public static int hig_closest(int number, int x = 0, int y = 0,
                                  int branch = 1)
    {
        int answer = -1;
        int num = Convert.ToInt32(Math.Pow(2, x) * Math.Pow(3, y));

        // ветвь становится листом в этой точке
        if (num >= number) { answer = num; }
        else
        {
            List<int> answers = new List<int>();

            answers.Add(hig_closest(number, x + 1, y, 0));
            if (branch == 1) 
            { answers.Add(hig_closest(number, x, y + 1, 1)); }
            
            answer = answers.Min();
        }

        return answer;
    }



    // находит ближайшее большее число нормального вида,
    // по упрощённому алгоритму
    public static int normal(int number)
    {
        int c = 1;
        bool run = true;

        // упрощает введёное число
        while (run)
        {
            run = false;

            if ((number % 2) == 0)
            {
                number /= 2;
                c *= 2;
                run = true;
            }
            if ((number % 3) == 0)
            {
                number /= 3;
                c *= 3;
                run = true;
            }
        }

        int ansver = c * hig_closest(number);
        return ansver;
    }



    // сокращает дробь
    public static (int, int) shorten(int numerator, int denominator)
    {
        int g = gcd(numerator, denominator);
        numerator /= g;
        denominator /= g;
        return (numerator, denominator);
    }



    // дробит дробь на все возможные комбинации двух дробей
    public static List<List<List<int>>> split(int numerator,
                                              int denominator)
    {
        List<List<List<int>>> ansver = new List<List<List<int>>>();

        // тривиальный случай, когда дробить нечего
        if (numerator < 3)
        {
            ansver.Add(new List<List<int>>
            { new List<int>{numerator, denominator} });
            return ansver;
        }

        // если условие не выполнится - тогда и только тогда
        // пойдёт остальная часть функции

        List<List<int>> this_row = new List<List<int>>();

        int a_0, b_0, a_1, b_1;
        for (int i = 1; i <= numerator / 2; i++)
        {
            this_row.Clear();

            // создаются сразу сокращённые пары дробей
            (a_0, b_0) = shorten(numerator - i, denominator);
            (a_1, b_1) = shorten(i, denominator);

            this_row.Add(new List<int> { a_0, b_0 });
            this_row.Add(new List<int> { a_1, b_1 });
            ansver.Add(new List<List<int>>(this_row));
        }

        return ansver;
    }



    // восстанавливает числитель начальной дроби по ряду
    public static int numerator_returner(List<List<int>> row)
    {
        int ansver = 0;
        List<int> denominators = new List<int>();

        foreach (List<int> fraction in row)
        {
            if (!(denominators.Contains(fraction[1])))
            {
                denominators.Add(fraction[1]);
            }
            else { return -1; } // ситуация с ошибочным рядом
        }

        // если else в цикле не отработает —
        // то тогда пойдёт остальная часть кода.
        // иначе — ряд ошибочен

        int m = lcm(denominators);
        foreach (List<int> fraction in row)
        {
            ansver += fraction[0] * m / fraction[1];
        }

        return ansver;
    }



    // проверяет на удобство построение конвейера
    public static bool common(List<List<int>> row)
    {
        // сортирует в порядке возрастания
        List<int> denominators = new List<int>();
        foreach (List<int> fraction in row)
        {
            denominators.Add(fraction[1]);
        }
        denominators.Sort();

        // проверяет на "последовательность"
        int a1, a2;
        bool ansver = true;
        for (int i = 1; (i < denominators.Count()) & ansver; i++)
        {
            a1 = denominators[i];
            a2 = denominators[i - 1];
            ansver &= (a1 % a2) == 0;
        }

        return ansver;
    }



    // кодирует дробь / ряд дробей в текст, для удобства чистки
    public static string codder(List<List<int>> list)
    {
        List<int> denominators = new List<int>();

        // сохраняет знаменатели входящего ряда
        foreach (List<int> fraction in list)
        {
            denominators.Add(fraction[1]);
        }

        string ansver = "";
        string numerator, denominator;
        int range = denominators.Count();

        // тривиальный случай, когда дробь лишь одна.
        if (range == 1)
        {
            numerator = Convert.ToString(list[0][0]);
            denominator = Convert.ToString(list[0][1]);
            ansver = numerator + "f" + denominator;
            return ansver;
        }

        // если условие не выполнится - тогда и только тогда
        // пойдёт остальная часть функции

        int m, j;
        for (int i = 0; i < range; i++)
        {
            // для игнорирования порядка дробей во входящем
            // ряду, следует начинать кодировку с дробей
            // с минимальным знаменателем
            m = denominators.Min();
            j = denominators.IndexOf(m);

            // вместо удаления, разумнее перезаписать текущую
            // ячейку памяти, а чтобы она не мешалась вдальнейшем,
            // её следует сделать больше максимальной.
            denominators[j] = denominators.Max() + 1;

            numerator = Convert.ToString(list[j][0]);
            denominator = Convert.ToString(list[j][1]);

            // добавляет разделительный символ между дробями
            if (i > 0) { ansver += "L"; }

            ansver += numerator + "f" + denominator;
        }

        return ansver;
    }



    // декодирует зашифрованную дробь / ряд дробей
    public static List<List<int>> decoder(string code)
    {
        List<List<int>> ansver = new List<List<int>>();

        // находит все дроби в ряду
        List<string> fractions = new List<string>(code.Split('L'));

        List<string> fraction = new List<string>();
        foreach (string codes in fractions)
        {
            fraction.Clear();

            // выделяет числитель и знаменатель дроби
            fraction.AddRange(codes.Split('f'));
            int numerator = Convert.ToInt32(fraction[0]);
            int denominator = Convert.ToInt32(fraction[1]);

            ansver.Add(new List<int> { numerator, denominator });
        }

        return ansver;
    }



    // очищает множество рядов от повторок
    // очищает множество рядов от повторок
    public static List<List<List<int>>> clean(List<List<List<int>>> data,
        int number)
    {
        List<List<List<int>>> ansver = new List<List<List<int>>>();

        string code;
        List<string> memory = new List<string>();

        // находит и убирает все повторки
        // так же проводит проверку на "удобность"
        foreach (List<List<int>> i in data)
        {
            if ((numerator_returner(i) == number) & common(i))
            {
                code = codder(i);
                if (!(memory.Contains(code)))
                {
                    memory.Add(code);
                    ansver.Add(new List<List<int>>(decoder(code)));
                }
            }
        }

        return ansver;
    }



    // находит все возможные способы финального расщепления
    // данной дроби на дробь / ряды дробей
    public static List<List<List<int>>> split_all(int numerator,
                                                   int denominator)
    {
        List<List<List<int>>> ansver = new List<List<List<int>>>();
        List<List<int>> this_row = new List<List<int>>();

        int a = numerator;
        int b = denominator;

        // тривиальный случай, когда некуда расщеплять
        if (a < 3)
        {
            this_row.Add(new List<int> { a, b });
            ansver.Add(new List<List<int>>(this_row));
            return ansver;
        }

        // если условие не выполнится - тогда и только тогда
        // пойдёт остальная часть функции

        List<List<List<int>>> this_variants =
            new List<List<List<int>>>();

        int a_0, b_0, a_1, b_1;
        for (int i = 1; i <= a / 2; i++)
        {
            // создаются сразу сокращённые пары дробей
            (a_0, b_0) = shorten(a - i, b);
            (a_1, b_1) = shorten(i, b);

            this_row.Add(new List<int> { a_0, b_0 });
            this_row.Add(new List<int> { a_1, b_1 });

            // первое расщепление сразу дало один из ответов
            if ((a_0 < 3) & (a_1 < 3))
            { ansver.Add(new List<List<int>>(this_row)); }
            else
            { this_variants.Add(new List<List<int>>(this_row)); }
            this_row.Clear();
        }

        // тривиальный случай, когда все первичные расщепления
        // стали финальными
        if (this_variants.Count() == 0) { return ansver; }

        // если условие не выполнится - тогда и только тогда
        // пойдёт остальная часть функции

        List<List<int>> new_row = new List<List<int>>();
        List<List<List<int>>> splitteners = // this_variants_1
            new List<List<List<int>>>();
        List<List<List<int>>> new_data = // this_variants_2
            new List<List<List<int>>>();
        List<List<List<int>>> cycle_data = // this_variants_3
            new List<List<List<int>>>(this_variants);
        int start;
        List<string> memory = new List<string>();



        // если глубина рекурсии превысит заданное значение -
        // нужно будет выйти из цыкла, 
        // ведь в нём самом уже ненужные цыклы
        int deep = 0;
        while ((deep < 500) & (cycle_data.Count() > 0))
        {
            deep++;

            // очистка от мусора с предыдущих цыклов
            cycle_data = new List<List<List<int>>>(
                clean(cycle_data, a)
            );
            splitteners.Clear();
            new_data.Clear();



            // процесс расщепления рядов
            foreach (List<List<int>> row in cycle_data)
            {
                // расщепление каждой дроби в ряду
                foreach (List<int> fraction in row)
                {
                    // дроби имеет смысл расщеплять только если
                    // их числитель превышает двойку
                    if (fraction[0] > 2)
                    {
                        // создание ряда без текущей дроби
                        new_row.Clear();
                        new_row.AddRange(new List<List<int>>(row));
                        new_row.Remove(fraction);

                        start = splitteners.Count();

                        // все расщепления текущей дроби
                        splitteners.AddRange(
                            new List<List<List<int>>>(
                                split(fraction[0], fraction[1])
                            )
                        );

                        // добавление к каждому из расщеплений текущей
                        // дроби все остальные непроверенные дроби
                        for (int i = start; i < splitteners.Count(); i++)
                        {
                            splitteners[i].AddRange(
                                new List<List<int>>(new_row)
                            );
                        }
                    }

                    // сохранение всех расщеплений для будующих вычислений
                    splitteners = new List<List<List<int>>>(
                        clean(splitteners, a)
                    );
                }
            } // расщепление


            cycle_data.Clear();

            int ok = 0;
            int ok_vars;
            string code;

            // проверка каждого ряда:
            // нужно ли его сохранить на будущие цыклы,
            // или же его нужно в ответ записать
            foreach (List<List<int>> row_1 in splitteners)
            {
                if ((numerator_returner(row_1) == a) & common(row_1))
                {
                    code = codder(row_1);
                    if (!(memory.Contains(code)))
                    {
                        memory.Add(code);

                        // проверяем количество "верных" дробей в ряду
                        ok_vars = 0;
                        foreach (List<int> fraction in row_1)
                        {
                            if (fraction[0] < 3) { ok_vars++; }
                        }

                        // если все дроби верные — то ряд финальный
                        if (ok_vars == row_1.Count())
                        {
                            ansver.Add(new List<List<int>>(decoder(code)));
                            ok++;
                        }
                        else
                        {
                            // сохранение в будущие цыклы на расщепление
                            cycle_data.Add(new List<List<int>>(
                                decoder(code)));
                        }
                    }
                }
            }

            if (ansver.Count() > 0)
            {
                ansver = new List<List<List<int>>>(clean(ansver, a));
            }



            if ((cycle_data.Count() == 0) & (ansver.Count() > 0))
            { return ansver; }
        } // главный цыкл



        if (ansver.Count() == 0) { return null; }
        else { return ansver; }
    }



    // вырисовывает набор рядов в консоль
    public static void print(List<List<List<int>>> data)
    {
        foreach (List<List<int>> matrix in data)
        {
            int count = 0;
            foreach (List<int> vector in matrix)
            {
                if (count > 0) { Console.Write(" + "); }
                count++;
                Console.Write($"{string.Join("/", vector)}");
            }
            Console.WriteLine(""); // New line after each sub-array
        }
    }



    // тупо для сокращения кода
    public static byte[] byter(string text)
    {
        return System.Text.Encoding.Default.GetBytes(text);
    }



    // тупо для сокращения кода
    public static string unbyter(byte[] bytes)
    {
        return System.Text.Encoding.Default.GetString(bytes);
    }



    // основная программа для произвольных данных
    public static void Main()
    {
        // ввод данных
        Console.Write("числитель: ");
        int a = Convert.ToInt32(Console.ReadLine());
        if (a < 1)
        {
            throw new Exception(
                "числитель должен быть строго больше нуля");
        }

        Console.Write("знаменатель: ");
        int b = Convert.ToInt32(Console.ReadLine());
        if (b <= a)
        {
            throw new Exception(
                "знаменатель должен быть строго больше числителя");
        }
        
        int a0, b0, a1, b1;
        (a, b) = shorten(a, b);
        b1 = normal(b);
        (a0, b0) = shorten(a, b1);
        
        // вывод конвейеров
        List<List<List<int>>> c = split_all(a0, b0);
        if (c != null)
        {
            c = new List<List<List<int>>>(clean(c, a0));
            print(c);

            // возвращённые конвейеры
            if (b1 - b > 0)
            {
                Console.WriteLine("delta");

                (a1, b1) = shorten(b1 - b, b1);

                List<List<List<int>>> delta = split_all(a1, b1);
                if (delta != null)
                {
                    delta = new List<List<List<int>>>(clean(delta, a1));
                    print(delta);
                }
                else
                {
                    Console.WriteLine(
                        "error. please try again in debug mode");
                }
            }
        }
        else
        {
            Console.WriteLine("error. please try again in debug mode");
        }

        Console.ReadLine();
    }
}