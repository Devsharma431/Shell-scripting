echo -n "Enter Left-End: " 
read le
echo -n "Enter Right-End: " 
read ri

is_prime(){ 
   if [ $1 -lt 2 ]; then 
       return 
   fi 
   ctr=0 
   for((i=2;i<$1;i++)){ 
       if [ $(( $1 % i )) -eq 0 ]; then 
           ctr=$(( ctr +1 )) 
       fi 
   }
   if [ $ctr -eq 0 ]; then 
       printf "%d " "$1" 
   fi 
}
printf "Prime Numbers between %d and %d are: " "$le" "$ri"
for((i=le;i<=ri;i++)){ 
   is_prime $i 
} 
printf "\n" 
