print('This is a string! {}'.format('This is something Ive inserted!'));

print('The {2} {1} {0}'.format('one', 'two', 'three'));
print('The {a} {b} {c}'.format(a='one', b='two', c='three'));

result = 100 / 7777;


# float : {value:width:precision}
print(result);
print('The result was {r:1.3f}'.format(r=result));
print('The result was {r:10.3f}'.format(r=result));

name = 'Jose';
name2 = 'Xorxe';

print(f'Hello! My name is {name}');
print(f'Hello! My name is {name} and my friend is {name2}');
