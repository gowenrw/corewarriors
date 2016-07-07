;redcode-94
;name test2
;author @alt_bier
;assert 1

chug		EQU	451

		ORG	drink

bomb	malt	DAT	$0,	$0
alt		MOV	bomb,	<malt
		DJN	alt,	malt
bier		DAT	$0,	$0

drink		ADD	#chug,	bier
		MOV	bomb,	>bier
		MOV	alt,	>bier
		MOV	alt+1,	@bier
		SPL	<bier
		JMP	drink
