class bc: 

	# https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences
	
	ESC        = '\033['
	M          = 'm'
	HEADER     = ESC + '95' + M
	ENDC       = ESC + '0' + M
	BOLD       = ESC + '1' + M
	UNDERLINE  = ESC + '4' + M
	UPBYN      = 'A'
	DOWNBYN    = 'B'
	UP         = ESC + 'A'
	DOWN       = ESC + 'B'
	CLEAR      = ESC + 'K'
	
	FGBLACK    = ESC + str(30) + M
	FGRED      = ESC + str(31) + M
	FGGREEN    = ESC + str(32) + M
	FGYELLOW   = ESC + str(33) + M
	FGBLUE     = ESC + str(34) + M
	FGMAGENTA  = ESC + str(35) + M
	FGCYAN     = ESC + str(36) + M
	FGWHITE    = ESC + str(37) + M

	BGBLACK    = ESC + str(40) + M
	BGRED      = ESC + str(41) + M
	BGGREEN    = ESC + str(42) + M
	BGYELLOW   = ESC + str(43) + M
	BGBLUE     = ESC + str(44) + M
	BGMAGENTA  = ESC + str(45) + M
	BGCYAN     = ESC + str(46) + M
	BGWHITE    = ESC + str(47) + M

	FGBBLACK   = ESC + str(90) + M
	FGBRED     = ESC + str(91) + M
	FGBGREEN   = ESC + str(92) + M
	FGBYELLOW  = ESC + str(93) + M
	FGBBLUE    = ESC + str(94) + M
	FGBMAGENTA = ESC + str(95) + M
	FGBCYAN    = ESC + str(96) + M
	FGBWHITE   = ESC + str(97) + M

	BGBBLACK   = ESC + str(100) + M
	BGBRED     = ESC + str(101) + M
	BGBGREEN   = ESC + str(102) + M
	BGBYELLOW  = ESC + str(103) + M
	BGBBLUE    = ESC + str(104) + M
	BGBMAGENTA = ESC + str(105) + M
	BGBCYAN    = ESC + str(106) + M
	BGBWHITE   = ESC + str(107) + M