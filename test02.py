#Return not values
#หมายถึง การสิ้นสุดหรือการจบการทำงานของ Black space การทำงานหนึ่งๆ เมื่อมันถูกทำงาน

def func1( ) :
    print('AAA')
    print('BBB')
    return
    print('CCC')

def func2( x ) :
    return
    print(f'X is {x}')

func1( )
func2( 10 )    