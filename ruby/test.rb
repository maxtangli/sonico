require 'test/unit'

class HelloTest < Test::Unit::TestCase
  def test_hello
    assert_equal('hello', %w{h e l l o}.join(''))
  end
end