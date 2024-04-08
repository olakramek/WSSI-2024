kobieta(fa).
mezczyzna(ma).
mezczyzna(md).
mezczyzna(mf).


lubi(jan, pawel).
lubi(pawel, krzysztof).
lubi(pawel, jan).
lubi(jan, bartek).
lubi(jan, ania).
lubi(bartek, jan).
lubi(ma, fa).
lubi(fa, ma).
lubi(mb, fb).
lubi(mc, fb).
lubi(md, mf).
lubi(mf, md).





przyjazn(X, Y) :-
lubi(X,Y),
lubi(Y,X).

niby_przyjazn(X,Y) :-
lubi(X,Y);
lubi(Y,X).

nieprzyjazn(X,Y) :-
\+lubi(X,Y),
\+lubi(X,Y).

loves(X, Y) :-
lubi(X, Y),
lubi(Y, X),
\+ (lubi(X, Z), Z \= Y),
\+ (lubi(Z, Y), Z \= X).

true_love(X, Y) :-
loves(X, Y),
loves(Y, X),
(
(kobieta(X), mezczyzna(Y));
(kobieta(Y),mezczyzna(X))
).

    
    
    
