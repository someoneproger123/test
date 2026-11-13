data = [
    ['Bangkok', 18180280, 'admin'], ['Karachi', 21422590, 'primary'],
    ['Bengaluru', 13187098, 'primary'],
]
out=list(filter(lambda x: x[2]=='primary' and x[1]>=10000000,data))
out=list(map(lambda x: x[0],out))
print(f'Cities: {', '.join(sorted(out))}')