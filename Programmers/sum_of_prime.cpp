#include <vector>
using namespace std;

long long solution(int N)
{
    long long answer = 0;
    vector<bool> arr(N + 1);

    for (int i = 2; i <= N; i++)
    {
        if (!arr[i])
        {
            answer += i;
            for (int j = i; j <= N; j += i)
            {
                arr[j] = true;
            }
        }
    }

    return answer;
}
