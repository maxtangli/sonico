# Eloquent Ruby.Russ Olsen.2011

class ClassA
  def hello
    puts 'hello'
    self
  end

end

a = ClassA.new


class ClassA
  # dynamic add method
  def world
    puts 'world'
    self
  end

  # renaming method
  alias_method :hi, :hello
  alias_method :こんにちは, :hello
  alias_method :你好, :hello
  # change visibility of method
  # remove_method :你好

  # class method to change class
  def self.set_region(region)
    case region
      when 'en'
        def hello
          puts 'hello'
        end
      when 'jp', 'ja'
        def hello
          puts 'こんにちは'
        end
      when 'cn'
        def hello
          puts '你好'
        end
      else
        raise ArgumentError, "Invalid region[#{region}]."
    end
  end
end

a.hello.world.hi.こんにちは.你好

ClassA.set_region('ja')
a.hello

ClassA.set_region('cn')
a.hello

class MostlyEmpty
  puts "The value of self is #{self}"
end