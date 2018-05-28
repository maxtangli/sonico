require 'csv'

module CsvParser
  extend self
  def read_csv(file)
    begin
      csv_array = CSV.read(file, 'r:BOM|UTF-8')
    rescue
      csv_array = CSV.read(file, encoding: "Shift_JIS:utf-8")
    end
    csv_array
  end
end
