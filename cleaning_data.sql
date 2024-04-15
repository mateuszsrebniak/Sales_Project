-- Mimo że doskonale znam źródło moich danych i nie spodziewam się większych problemów, to sprawdzić kilka rzeczy
-- W SQL Developer w zakładce 'Statistics' znajdziemy krótkie podsumowanie dla wszystkich tabel i kolumn
        -- I już na pierwszy rzut oka widzę, że w tabeli 'Orders' mam:
                --  jeden rekord z wartością NULL
                --  w kolumnach 'is_inside_cleaning' oraz 'is_outside_cleaning' znajdują się po cztery różne
                        --  wartości, choć powinny znajdować się po dwie: True lub False
                --  w kolumnach 'is_inside_cleaning' oraz 'is_outside_cleaning' znajdować mogą się wyłącznie
                        -- wartości True lub False i skoro doszło do realizacji, to przynajmniej jedna z kolumn
                        -- powinna zawierać wartość True. Znajduję jednak rekordy, gdzie obie kolumny mają
                        -- wartość False
        -- W tabeli 'Customers':
                --  przy 1088 różnych klientach znajduje się tylko 1086 unikatowych adresów e-mail

-- PROBLEM: 
        -- rekord z wartością NULL
-- ROZWIĄZANIE:
        -- usunięcie rekordu. Był to rekord testowy, nie zawierał żadnych przydatnych informacji
DELETE FROM orders
WHERE order_id IN (
            SELECT order_id
            FROM orders
            WHERE is_inside_cleaning is null
    );

-- PROBLEM: 
        --  w kolumnach 'is_inside_cleaning' oraz 'is_outside_cleaning' znajdują się po cztery różne
        --  wartości, choć powinny znajdować się po dwie: True lub False
-- ROZWIĄZANIE:
        -- Wartościami poza True i False były wartości 1 oraz 0. Problem wziął się stąd, że kolumny są
        -- kolumnami tekstowymi, natomiast kod w Pythonie generuje wartości logiczne True i False, toteż
        -- gdy mój skrypt wstawiał rekordy, podmieniał wartość True na 1, a False na 0.
        -- Naprawiłem to zmieniając kod w Pythonie z:
                -- self.is_inside_cleaning = random.choices([True', False], [0.96, 0.04], k=1)[0]
                -- self.is_outside_cleaning = random.choices([True', False], [0.22, 0.78], k=1)[0]
        -- na:
                -- self.is_inside_cleaning = random.choices(['True', 'False'], [0.96, 0.04], k=1)[0]
                -- self.is_outside_cleaning = random.choices(['True', 'False'], [0.22, 0.78], k=1)[0]
        -- oraz dokonując UPDATE na tabeli, który zamienił wszystkie 1 na 'True', a 0 na 'False'
UPDATE orders 
SET 
    is_inside_cleaning = 
    CASE 
        WHEN is_inside_cleaning = '1' THEN 'True'
        WHEN is_inside_cleaning = '0' THEN 'False'
        ELSE is_inside_cleaning
    END,
    is_outside_cleaning = 
    CASE 
        WHEN is_outside_cleaning = '1' THEN 'True'
        WHEN is_outside_cleaning = '0' THEN 'False'
        ELSE is_outside_cleaning
    END;

-- PROBLEM: 
        -- przy 1088 unikatowych klientach znajduje się tylko 1086 unikatowych adresów e-mail
-- ROZWIĄZANIE:
        -- sprawdzić, czy dane się nie duplikują, być może jest to wynik zduplikowanych rekordów
        -- sprawdzić, czy klienci nie są przedstawicielami tej samej firmy i czy nie podali tego samego e-maila
        -- sprawdzić, czy zduplikowane maile nie są wynikiem błędu, literówki itd.
        -- jeśli jest możliwość - poprawić adresy email.
        -- sprawdzić, czy wszyscy klienci są klientami aktywnymi, czy zamawiają sprzątanie
        -- osatecznie ocenić, czy w danym projekcie adresy e-mail będą potrzebne do realizacji celu.
        -- w moim przypadku adresy email nie są potrzebne

--PROBLEM:
        --  w kolumnach 'is_inside_cleaning' oraz 'is_outside_cleaning' znajdować mogą się wyłącznie
        -- wartości True lub False i skoro doszło do realizacji, to przynajmniej jedna z kolumn
        -- powinna zawierać wartość True. Znajduję jednak rekordy, gdzie obie kolumny mają
        -- wartość False
--ROZWIĄZANIE:
        -- Problem ma swoje źródło w kodzie Python generującym kolejne rekordy. Nie uwzględniłem tam warunku
        -- mówiącego, że przynajmniej jedna kolumna musi mieć wartość True
        -- Do kodu w Python dodałem warunek if:
        if not self.is_inside_cleaning and not self.is_outside_cleaning:
            self.is_inside_cleaning = True
        -- Zostawię jednak błędne dane w swoim zbiorze, by w ramach nauki mieć problem do nauki.
        -- Ostatecznie uznałem, że bezpieczniej będzie każdemu takiemu problematycznemu rekordowi
        -- przypisać niższą wartość. Pomoże to uniknąć przeszacowania sprzedaży.