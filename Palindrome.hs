isPalindrome :: Int -> Bool
isPalindrome x = let xString = show x
                     bytes = map (toEnum . fromEnum) xString :: [Word8]
                     dim = length bytes
                 in all (\i -> bytes !! i == bytes !! (dim - i - 1)) [0..(dim `div` 2 - 1)]
