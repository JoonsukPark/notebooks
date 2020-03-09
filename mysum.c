long long mysum_int(int n, long long* array) {
    long long res = 0;
    for (int i=0; i<n; i++)
        res += array[i]*array[i];
    return res;
}

double mysum_double(int n, double* array) {
    double res = 0;
    for (int i=0; i<n; i++)
        res += array[i]*array[i];
    return res;
}
