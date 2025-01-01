### what is important for this calculator to work?

> So a calcultor can take in numbers and operate them
> Taking in the numbers would be done by puttin them in an array and operate on them
> so

[1, 2, 3 ,4 ,5]
[n, n+1, n+2, n+3, n+4, n+n]

> We could use a for loop for the length of the array
> So an addition would be adding the first index to the next one etc.

result = 0
for (let i = 0; i < length(array); i++){
result += array[i]
}
return result

> For a substraction it would be remove the second number from the first number and from the
> result of that remove the next index
> then return the first index

for (let i = 1; i < length(array); i++){
array[0] -= array[i]
}
return array[0]

> For a multiplication it would be to multiply the first number with the second and then
> the result of that with the next one
> then return the first index

for (let i = 1; i < length(array); i++){
array[0] \*\*\*\*= array[i]
}
return array[0]

> For a division it would be to divide the first number with the second number and then the result
> with the next number (index)
> then return the first index

    for (let i = 1; i < length(array); i++){
        array[0] /= array[i]
    }

return array[0]
