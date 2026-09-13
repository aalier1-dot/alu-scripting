#!/usr/bin/env ruby
log_line = ARGV[0].to_s
if log_line =~ /\[from:([^\]]*)\]\s\[to:([^\]]*)\]\s\[flags:([^\]]*)\]/
  puts "#{$1},#{$2},#{$3}"
end
