#include <bits/stdc++.h>
using namespace std;
#define SPEED ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef long long ll;
#define fe first
#define se second
#define pb push_back
#define sz(a) int((a).size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define sortt(a) sort(a.begin(),a.end());
#define all(v) v.begin(), v.end()
#define vii vector<int> 
#define vll vector<long long> 
#define vpi vector<PII> 
long long M=1e9+7;
ll power(ll x, ll y, ll m=M) 
{ 
    if (y == 0) 
        return 1; 
    ll p = power(x, y/2LL, m) % m; 
    p = (p * p) % m; 
  
    return (y%2LL == 0)? p : (x * p) % m; 
} 
 
ll modInverse(ll a, ll m) 
{ 
	return power(a, m-2LL, m); 
} 

int gcd(int a, int b){
    if(a<b)swap(a,b);
    while(b>0){
        int tmp = b;
        b = a%b;
        a = tmp;
    }
    return a;
}

/*************************************************/

void solve(){
    
}

void solveall(){
    int t; cin>>t;
    while(t--){
        solve();
    }
}

int main(){
    solveall();
    return 0;
}