isLeapYear:: Int -> String
isLeapYear y = if ((y `mod` 4 == 0) && (y `mod` 100 /=0)) || (y `mod` 100 == 0 && y `mod` 400 == 0) then "leap year" else "not leap year"
main :: IO ()
main = do
    let year = 1900
    print $ isLeapYear year
