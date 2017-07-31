# Eloquent Ruby.Russ Olsen.2011

require 'text' # From the text gem
class DocumentErrorHandling
  include Text

  def method_missing(missing, *args)
    candidates = methods_that_sound_like(missing.to_s)
    message = "You called an undefined method: #{missing}."
    unless candidates.empty?
      message += "\nDid you mean #{candidates.join(' or ')}?"
    end
    raise raise NoMethodError.new(message)
  end

  def methods_that_sound_like(name)
    missing_soundex = Soundex.soundex(name.to_s)
    public_methods.sort.find_all do |existing|
      existing_soundex = Soundex.soundex(existing.to_s)
      missing_soundex == existing_soundex
    end
  end

  # const??
  def self.const_missing(const_name)
    msg = %Q{
      You tried to reference the constant #{const_name}
      There is no such constant in the Document class.
    }
    raise msg
  end

end

DocumentErrorHandling.new.methodd