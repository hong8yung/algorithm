#include <vector>

using namespace std;
bool chk_prime(int x){
    if(x<2) return false;
    for(int i=2; i<=(int)(x/2); i++){
        if(x%i==0) return false;
    }
    
    return true;
}
long long solution(int N) {
    long long answer = 0;
    for(int i=2; i<=N; i++){
        if(chk_prime(i)){
            answer += i;
        }
    }
    return answer;
}
