def fact(n)
 n==0?1:n*fact(n-1)
end

puts fact(ARGV[0].to_i)
