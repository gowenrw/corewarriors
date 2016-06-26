;redcode-94
;name test2
;author @alt_bier
;assert 1

;a	org	start
;a bomb	DAT	#0,	#0
;a 	SPL	0
;a start	ADD 	#4, 	bomb
;a 	MOV 	bomb, 	@bomb
;a 	JMP	start
;a 
;a 	END	start

	ORG	lOOp

	iSt	EQU	(Posi+3039)
	sSt	EQU	(Poss+3357)

mGo:	SPL	2,	>-200
	SPL	2,	>-350
	MOV	<bombA,	{Posi
	MOV	<bombB, {Poss
Poss:	JMP	sSt+5	5
Posi:	JMP	iSt+5	>-550

bombA:	DAT	0,	1
bombB:	MOV	0,	1
	
lOOp:	MOV	0,	1
	JMP	lOOp

