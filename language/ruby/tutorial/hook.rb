# Eloquent Ruby.Russ Olsen.2011

# self.inherited
class SimpleBaseClass
  # maybe used to iterate subclass to find useful one,
  # e.g. DocumentReader.read(path), class SimpleTest < Test::Unit::TestCase
  def self.inherited(new_subclass)
    puts "Hey #{new_subclass} is now a subclass of #{self}!"
  end
end

class ChildClass < SimpleBaseClass
end

class ChildChildClass < ChildClass
end

# self.included
module SimpleModule
  def self.included(klass)
    puts "Hey, #{self} has been included in #{klass}"
  end
end

class MixClass
  include SimpleModule
end

# at_exist stack
at_exit {puts 'See you, ruby metaprogramming: hook.!'}
at_exit {puts 'That\'s all!'}

# set_trace_func
proc_object = proc do |event, file, line, id, binding, klass|
  puts "#{event} in #{file}/#{line} #{id} #{klass}"
end
set_trace_func(proc_object)