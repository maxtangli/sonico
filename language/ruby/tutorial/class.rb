module HelloClass
  class HelloSayAble
    attr_reader :name

    def initialize(name)
      @name = name
    end

    def say_hello
      puts "%s said, \"%s!\"\n" % [name, message]
    end
  end
end

include HelloClass

module HelloClass
  class Englishman < HelloSayAble
    def message
      "hello"
    end
  end

  class Japanese < HelloSayAble
    def message
      "こんにちは"
    end
  end
end

Englishman.new('Sherlock Holmes').say_hello
Japanese.new('Richard Moore').say_hello