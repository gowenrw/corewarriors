;redcode-94
;name test
;author @alt_bier
;assert 1

	org	start

bomb	DAT	#0,	#0
	SPL	0

start	ADD 	#4, 	bomb
	MOV 	bomb, 	@bomb
	JMP	start

	END	start
