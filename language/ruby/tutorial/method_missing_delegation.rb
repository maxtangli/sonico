# Eloquent Ruby.Russ Olsen.2011

class DocumentDelegate
  def initialize(original_document, time_limit_seconds)
    @original_document = original_document
    @time_limit_seconds = time_limit_seconds
    @create_time = Time.now
  end

  def time_expired?
    Time.now - @create_time >= @time_limit_seconds
  end

  def check_for_expiration
    raise 'Document no longer available' if time_expired?
  end

  DELEGATED_METHODS = [:content, :words, :length]

  def method_missing(name, *args)
    check_for_expiration
    if DELEGATED_METHODS.include?(name)
      @original_document.send(name, *args)
    else
      super
    end
  end
end

string = 'Good morning, Mr. Phelps'
secret_string = DocumentDelegate.new(string, 2)
puts secret_string.length
sleep 2
puts secret_string.length