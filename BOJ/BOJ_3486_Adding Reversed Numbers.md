## 문제
The Antique Comedians of Malidinesia prefer comedies to tragedies. Unfortunately, most of the ancient plays are tragedies. Therefore the dramatic advisor of ACM has decided to transfigure some tragedies into comedies.The Antique Comedians of Malidinesia prefer comedies to tragedies. Unfortunately, most of the ancient plays are tragedies. Therefore the dramatic advisor of ACM has decided to transfigure some tragedies into comedies. Obviously, this work is very hard because the basic sense of the play must be kept intact, although all the things change to their opposites. For example the numbers: if any number appears in the tragedy, it must be converted to its reversed form before being accepted into the comedy play.

Reversed number is a number written in arabic numerals but the order of digits is reversed. The first digit becomes last and vice versa. For example, if the main hero had 1245 strawberries in the tragedy, he has 5421 of them now. Note that all the leading zeros are omitted. That means if the number ends with a zero, the zero is lost by reversing (e.g. 1200 gives 21). Also note that the reversed number never has any trailing zeros.

ACM needs to calculate with reversed numbers. Your task is to add two reversed numbers and output their reversed sum. Of course, the result is not unique because any particular number is a reversed form of several numbers (e.g. 21 could be 12, 120 or 1200 before reversing). Thus we must assume that no zeros were lost by reversing (e.g. assume that the original number was 12).

## 해석
Malidnesia의 Antique 코미디언들은 비극보다는 코미디를 더 좋아한다. 불행히도, 고대 연극의 대부분은 비극이다. 그래서 ACM의 연극 고문은 몇 가지 비극을 희극으로 개조하기로했다. 분명히, 모든 것이 바뀌지만 연극의 기본 감각은 그대로 유지되어야하기 때문에 이 작업은 매우 힘들다: 만약 비극에 어떤 숫자가 나타난다면, 이는 코미디에 받아들여지기 전에 역전된 형태로 전환되어야 한다.

역전된 숫자는 아라비아 숫자로 쓰여져있지만 자릿수의 순서는 역전된다. 처음 숫자는 마지막이되고 그 반대가 된다. 예를들어, 만약 비극에서 주인공이 1245개의 딸기를 갖고 있다면,그는 5421개를 갖고 있는 것이 된다. 0으로 시작되는 것은 모두 생략함을 유의한다. 즉, 0으로 끝나는 숫자의 경우, 역순이 된 숫자에서 0을 생략한다(예: 1200은 21). 또한 반전된 숫자는 절대 0으로 끝나지 않는다는 것을 유의한다.

ACM은 역전된 숫자로 계산해야 한다. 니가 해야할 것은 두개의 역전된 숫자를 더하고 그 반되로된 합을 출력하는 것이다. 물론, 어떤 특정한 숫자가 여러개의 역전된 숫자이기 때문에 결과는 하나만 존재하는 것이 아니다(예: 21은 역방향 전 12, 120, 1200일 수 있음). 또한 우리는 역전으로 인해 0이 상실되지 않았다고 가정해야한다.(예: 원래 숫자가 12였다고 가정).

#### 입력
입력은 N개의 케이스로 구성된다. 첫 번째 줄에는 양의 정수 N이 입력된다. 그 후로 케이스들이 입력된다. 각 케이스는 공백을 기준으로 두 개의 양의 정수가 주어진다. 이 수들은 니가 추가해야 할 역수들이다. 두 개의 정수는 10만보다 작은 수 이다.

#### 출력
각 케이스에 대해, 한개만 정수씩을 출력한다. 두 개의 역수의 역 합계를 출력하며 출력에서 0을 모두 생략하라.