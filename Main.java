import java.io.*;
import java.util.*;

// https://www.acmicpc.net/problem/2167
// 2차원 배열의 합

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st  = new StringTokenizer(br.readLine()," ");   
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int [][] arr = new int[N+1][M+1];
        int [][] dp = new int[N+1][M+1];

        for(int i = 1 ; i <= N ; i++){
            for(int j = 1 ; j <= M ; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]; 
            }
        }

        int K = Integer.parseInt(br.readLine());

        for(int i = 0 ; i < K ; i++){
            
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            System.out.println(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]);
        }

    }
}
