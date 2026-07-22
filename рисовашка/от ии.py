"""
from fractions import Fraction

def find_fractions(total_input, target_output):
    fractions = []
    current_total = total_input
    remainder = current_total

    while remainder > 0 and len(fractions) < 10:  #лимит для предотвращения бесконечного цикла
        
        # Получаем внутреннюю долю для текущего потока
        extracted = target_output / (total_input / current_total)

        # Если переведенный поток меньше чем 1, просто запрашиваем простую дробь
        if extracted >= 1:
            f = extracted
            fractions.append(Fraction(f).limit_denominator())
            remainder -= target_output
            break
            
        # Резервируем дробь и уменьшаем оставшийся остаток
        fractions.append(Fraction(extracted).limit_denominator())
        remainder -= extracted

    return fractions

def get_resources(max_capacity, incoming, desired_output):
    if desired_output > incoming or desired_output * 3 > max_capacity:
        return None  # Невозможно выполнить задачу

    # Находим дроби
    fractions = find_fractions(incoming, desired_output)

    return fractions


# Примеры вызова функции
max_capacity = 1000
incoming_flow_1 = 16
desired_output_1 = 4
print(get_resources(max_capacity, incoming_flow_1, desired_output_1))

incoming_flow_2 = 18
desired_output_2 = 5
print(get_resources(max_capacity, incoming_flow_2, desired_output_2))

incoming_flow_3 = 50
desired_output_3 = 10
print(get_resources(max_capacity, incoming_flow_3, desired_output_3))
"""



from fractions import Fraction
from itertools import combinations_with_replacement

def find_fractions(input_amount, desired_output, tracker, max_capacity):
    results = []

    # Известно, что выход может быть меньше или равен текущему входу
    if desired_output > input_amount:
        return results

    # Проверяем, если нужное количество ресурсов равно нулю
    if desired_output == 0:
        return [("0", [])]

    # Поиск сочетания дробей
    max_numerator = min(input_amount, max_capacity)
    for i in range(1, max_numerator + 1):
        for fraction in combinations_with_replacement(range(1, max_capacity + 1), i):
            total = Fraction(0)
            for num in fraction:
                if num <= input_amount:
                    total += Fraction(1, num)
            if total == Fraction(desired_output, input_amount):
                results.append((fraction, [str(Fraction(1, num)) for num in fraction]))

    return results

max_capacity = 1000  # Максимальная пропускная способность конвейера
input_amounts = [16, 18, 50]  # Примеры входного потока
desired_outputs = [6, 5, 10]  # Желаемые выходные значения

for input_amount, desired_output in zip(input_amounts, desired_outputs):
    print(f"Input: {input_amount}, Desired Output: {desired_output}")
    results = find_fractions(input_amount, desired_output, [], max_capacity)
    print(results)
    if results:
        for fraction, descriptions in results:
            print("Combination: ", ' + '.join(descriptions))
    else:
        print("No valid fractions found.")


















    
