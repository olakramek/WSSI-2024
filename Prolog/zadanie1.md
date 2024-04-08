# Zadanie 1

### A rodzeństwo

```prolog
 /* rodzicem(x,y) rodzicem x jest y */
rodzicem(x,a).
rodzicem(x,b).
rodzicem(y,a).
rodzicem(y,b).
rodzicem(z,a).

rodzenstwo_rodzone(X,Y) :-
    
  rodzicem(X,A),
  rodzicem(Y,A),
	rodzicem(X,B),
	rodzicem(Y,B),
    A\=B.
```

### B rodzeństwo cioteczne

```prolog
rodzicem(x,a).
rodzicem(a,c).
rodzicem(y,b).
rodzicem(b,c).

rodzenstwo_cioteczne(X, Y) :-
    rodzicem(X, A),
    rodzicem(A, C),
    rodzicem(Y, B),
    rodzicem(B, C),
    A \= C,
    B \= C,
    A \= B.

```

## C mają wspólnego wnuka

```prolog
rodzicem(c,a).
rodzicem(a,x).
rodzicem(c,b).
rodzicem(b,y).

wspolny_wnuk(X,Y) :-
    rodzicem(C,A),
    rodzicem(A,X),
    rodzicem(C,B),
    rodzicem(B,Y),
     A \= C,
    B \= C,
    A \= B.

    

```

## D rodzic przyrodni

```prolog
rodzicem(x,a).
rodzicem(b,a).
rodzicem(b,y).

rodzic_przyrodni(X,Y) :-
    rodzicem(X,A),
    rodzicem(B,A),
    rodzicem(B,Y),
    A\=X,
    A\=Y,
    B\=X,
    B\=Y,
    B\=A.
    
```

## E rodzeństwo przyrodnie

```prolog
rodzicem(x,a).
rodzicem(x,b).
rodzicem(y,b).
rodzicem(y,c).

rodzenstwo_przyrodne(X,Y) :-
    rodzicem(X,A),
    rodzicem(X,B),
    rodzicem(Y,B),
    rodzicem(Y,C),
    A\=X,
    A\=Y,
    B\=X,
    B\=Y,
    C\=X,
    C\=Y,
    A\=B,
	A\=C,
    B\=C.
```

## F rodzeństwo partnera

```prolog
rodzicem(a,x).
rodzicem(a,b).
rodzicem(b,c).
rodzicem(y,c).

rodzenstwo_partnera(X,Y) :-
    rodzicem(A,X),
    rodzicem(A,B),
    rodzicem(B,C),
    rodzicem(Y,C),
    A\=X,
    A\=Y,
    B\=X,
    B\=Y,
    C\=X,
    C\=Y,
    A\=B,
	A\=C,
    B\=C.
    
```

## G  rodzeństwo przyrodnie 2

```prolog
rodzicem(x,a).
rodzicem(x,b).
rodzicem(c,b).
rodzicem(y,c).
rodzicem(y,a).

rodzenstwo_przyrodnie_2(X,Y) :-
    rodzicem(X,A),
    rodzicem(X,B),
    rodzicem(C,B),
    rodzicem(Y,A),
    rodzicem(Y,C),
    A\=X,
    A\=Y,
    B\=X,
    B\=Y,
    C\=X,
    C\=Y,
    A\=B,
	A\=C,
    B\=C.
```