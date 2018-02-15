# http://cp1.nintendo.co.jp/code/ruby/first_page.txt
# KEY = ??
#
# def trans_table
#   alphabets = ["A".."Z", "a".."z", "0".."9"].map{|r| r.to_a.join}
#   alphabets.map{|ab| [ab, ab[KEY%ab.size..-1] + ab[0, KEY%ab.size]]}.
#       transpose.map{|a| a.join}
# end
#
# def decode(the_answer)
#   the_answer.tr *trans_table
# end
#
# if __FILE__ == $0
#   puts decode("ykkg://tg2.ezekveuf.tf.ag/vekvi")
# end

def trans_table(key)
  alphabets = ["A".."Z", "a".."z", "0".."9"].map {|r| r.to_a.join}
  alphabets.map {|ab| [ab, ab[key%ab.size..-1] + ab[0, key%ab.size]]}.
      transpose.map {|a| a.join}
end

def decode(the_answer, key)
  the_answer.tr *trans_table(key)
end

def find_key()
  encoded = 'ykkg://tg2.ezekveuf.tf.ag/'
  expected = 'http://cp1.nintendo.co.jp/'
  for key in 1..1000
    decoded = decode(encoded, key)
    return key if decoded==expected
  end
  'failed'
end

puts find_key
puts decode("ykkg://tg2.ezekveuf.tf.ag/vekvi", find_key) if find_key != 'failed'