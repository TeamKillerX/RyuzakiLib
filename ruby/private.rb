class PrivateApiUrl
  def initialize(url = "private.randydev.my.id", method = nil, punctuation = "?", parameter = nil, allow_web = "https")
    @url = url
    @method = method
    @punctuation = punctuation
    @parameter = parameter
    @allow_web = allow_web
  end

  def checking
    api_url = @allow_web + ":"
    api_url
  end
end

obj = PrivateApiUrl.new
result = obj.checking
puts result
