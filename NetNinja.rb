#If you are reading this you are doing is LIVE in NETNINJA Version Jumanji!!

#a special thanks to rubyfu.net for their awesome book I took so so much from

require 'readline'

#prevent ctrl+c for exiting

trap('INT', 'SIG_IGN')

#list of commands this section will be huge someday...

CMDS = ['help', 'clear', '!', 'irb', 'beastmode', 'python', 'exit'].sort

completion = 
	
	proc do |str|
		case
		when Readline.line_buffer =~/help.*/i
	puts "Available Commands: \n" + "#{CMDS.join("\t")}"
		when Readline.line_buffer =~/clear.*/i
	system 'clear'
		when Readline.line_buffer =~ /!.*/i
	puts ">>>>>>GET READY<<<<<<"
	STDOUT.flush
	beanfook = gets.chomp
	system beanfook
		when Readline.line_buffer =~ /irb.*/i
	system 'pry --simple-prompt'
		when Readline.line_buffer =~ /beastmode.*/i
	system 'cd /root/fluxion; bash fluxion'
		when Readline.line_buffer =~ /python.*/i
	system 'python -v'
		when Readline.line_buffer =~ /exit.*/i
	puts "exiting..."
	exit 0
		else
	CMDS.grep(/^#{Regexp.excape(str)}/i) unless str.nil?
		end
	end

Readline.completion_proc = completion #set completion process
Readline.completion_append_character = ' ' #make sure that space is there

while line = Readline.readline('<:NetNinja:>', true) #start console with character and make add_hist = true
	puts completion.call
	break if line =~ /^quit.*/i or line =~ /^exit.*/i
end
