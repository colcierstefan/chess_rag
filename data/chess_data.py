from models.chess_game import ChessGame

GAMES = [
    ChessGame(
        "1",
        "Adolf Anderssen",
        "Lionel Kieseritzky",
        """1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8. Nh4 Qg5 
        9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15. Bxf4 Qf6 
        16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21. Nxg7+ Kd8 
        22. Qf6+ Nxf6 23. Be7# 1-0""",
        "King's Gambit Accepted",
        "1-0",
        1851,
        "The Immortal Game"
    ),
    ChessGame(
        "2",
        "Donald Byrne",
        "Bobby Fischer",
        """1. Nf3 Nf6 2. c4 g6 3. Nc3 Bg7 4. d4 O-O 5. Bf4 d5 6. Qb3 dxc4 7. Qxc4 c6 8. e4 Nbd7 
        9. Rd1 Nb6 10. Qc5 Bg4 11. Bg5 Na4 12. Qa3 Nxc3 13. bxc3 Nxe4 14. Bxe7 Qb6 
        15. Bc4 Nxc3 16. Bc5 Rfe8+ 17. Kf1 Be6 18. Bxb6 Bxc4+ 19. Kg1 Ne2+ 20. Kf1 Nxd4+ 
        21. Kg1 Ne2+ 22. Kf1 Nc3+ 23. Kg1 axb6 24. Qb4 Ra4 25. Qxb6 Nxd1 26. h3 Rxa2 
        27. Kh2 Nxf2 28. Re1 Rxe1 29. Qd8+ Bf8 30. Nxe1 Bd5 31. Nf3 Ne4 32. Qb8 b5 
        33. h4 h5 34. Ne5 Kg7 35. Kg1 Bc5+ 36. Kf1 Ng3+ 37. Ke1 Bb4+ 38. Kd1 Bb3+ 
        39. Kc1 Ne2+ 40. Kb1 Nc3+ 41. Kc1 Rc2# 0-1""",
        "Grunfeld Defense",
        "0-1",
        1956,
        "Game of the Century"
    ),
    ChessGame(
        "3",
        "Paul Morphy",
        "Duke of Brunswick & Count Isouard",
        """1. e4 e5 2. Nf3 d6 3. d4 Bg4 4. dxe5 Bxf3 5. Qxf3 dxe5 6. Bc4 Nf6 7. Qb3 Qe7 
        8. Nc3 c6 9. Bg5 b5 10. Nxb5 cxb5 11. Bxb5+ Nbd7 12. O-O-O Rd8 13. Rxd7 Rxd7 
        14. Rd1 Qe6 15. Bxd7+ Nxd7 16. Qb8+ Nxb8 17. Rd8# 1-0""",
        "Philidor Defense",
        "1-0",
        1858,
        "The Opera Game"
    ),
    ChessGame(
        "4",
        "Garry Kasparov",
        "Deep Blue",
        """1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 5. Ng5 Ngf6 6. Bd3 e6 7. N1f3 h6 
        8. Nxe6 Qe7 9. O-O fxe6 10. Bg6+ Kd8 11. Bf4 b5 12. a4 Bb7 13. Re1 Nd5 
        14. Bg3 Kc8 15. axb5 cxb5 16. Qd3 Bc6 17. Bf5 exf5 18. Rxe7 Bxe7 19. c4 1-0""",
        "Caro-Kann Defense",
        "1-0",
        1997,
        "Kasparov vs Deep Blue, Game 1"
    ),
    ChessGame(
        "5",
        "Deep Blue",
        "Garry Kasparov",
        """1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Nd7 5. Ng5 Ngf6 6. Bd3 e6 7. N1f3 h6 
        8. Nxe6 Qe7 9. O-O fxe6 10. Bg6+ Kd8 11. Bf4 b5 12. a4 Bb7 13. Re1 Nd5 
        14. Bg3 Kc8 15. axb5 cxb5 16. Qd3 Bc6 17. Bf5 exf5 18. Rxe7 Bxe7 19. c4 1-0""",
        "Sicilian Defense",
        "1-0",
        1997,
        "Deep Blue vs Kasparov, Game 6"
    ),
    ChessGame(
        "6",
        "Mikhail Tal",
        "Vasily Smyslov",
        """1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 6. Bc4 e6 7. Bb3 b5 
        8. O-O b4 9. Na4 Nxe4 10. f3 d5 11. fxe4 dxe4 12. Be3 Nc6 13. Nxc6 Qxd1 
        14. Raxd1 e3 15. Rd7 Bb7 16. Nxb4 Bxg2 17. Nc6 Kd8 18. Rfd1+ Bd6 19. Nd4 1-0""",
        "Sicilian Defense",
        "1-0",
        1959,
        "Candidates Tournament"
    ),
    ChessGame(
        "7",
        "Magnus Carlsen",
        "Viswanathan Anand",
        """1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 5. d4 Nd6 6. Bxc6 dxc6 7. dxe5 Nf5 
        8. Qxd8+ Kxd8 9. h3 Ke8 10. Nc3 h5 11. Bf4 Be7 12. Rad1 Be6 13. Ng5 Rh6 
        14. g3 Bxg5 15. Bxg5 Rg6 16. h4 f6 17. exf6 gxf6 18. Bf4 Nxh4 19. f3 Rd8 
        20. Kf2 Rxd1 21. Nxd1 Nf5 22. Ne3 Nxe3 23. Bxe3 b6 24. Rh1 h4 25. Bd4 Rg7 1-0""",
        "Ruy Lopez",
        "1-0",
        2013,
        "World Championship"
    ),
    ChessGame(
        "8",
        "Bobby Fischer",
        "Boris Spassky",
        """1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bc4 e6 7. Bb3 Be7 
        8. Be3 O-O 9. O-O Na5 10. f4 b6 11. f5 Nxb3 12. axb3 exf5 13. Rxf5 Ne8 
        14. Qg4 Bh4 15. Raf1 Be7 16. Rf6 Nf6 17. Rxf6 Bxf6 18. Rxf6 Qe8 19. Rxd6 1-0""",
        "Sicilian Defense",
        "1-0",
        1972,
        "World Championship Match, Game 6"
    ),
    ChessGame(
        "9",
        "Anatoly Karpov",
        "Garry Kasparov",
        """1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 Nc6 5. Nb5 d6 6. c4 Nf6 7. N1c3 a6 
        8. Na3 d5 9. cxd5 exd5 10. exd5 Nb4 11. Be2 Bc5 12. O-O O-O 13. Bf3 Bf5 
        14. Bg5 Re8 15. Qd2 b5 16. Rad1 Nd3 17. Nab1 h6 18. Bh4 b4 19. Na4 Bd6 
        20. Bg3 Rc8 21. b3 g5 22. Bxd6 Qxd6 23. g3 Nd7 24. Bg2 Qf6 25. a3 a5 
        26. axb4 axb4 27. Qa2 Bg6 28. d6 g4 29. Qd2 Kg7 30. f3 Qxd6 31. fxg4 Qd4+ 
        32. Kh1 Nf6 33. Rf4 Ne4 34. Qxd3 Nf2+ 35. Rxf2 Bxd3 36. Rfd2 Qe3 37. Rxd3 Rc1 
        38. Nb2 Qf2 39. Nd2 Rxd1+ 40. Nxd1 Re1+ 0-1""",
        "Sicilian Defense",
        "0-1",
        1985,
        "World Championship Match"
    ),
    ChessGame(
        "10",
        "Viswanathan Anand",
        "Vladimir Kramnik",
        """1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 d5 5. cxd5 Qxd5 6. Nf3 Qf5 7. Qb3 Nc6 
        8. Bd2 O-O 9. h3 b6 10. g4 Qg6 11. Rg1 Bb7 12. a3 Bxc3 13. Bxc3 Ne4 14. Rg3 
        Nxc3 15. bxc3 Na5 16. Qc2 Nc4 17. e3 Rfd8 18. Bd3 Nxe3 19. fxe3 Qxg4 
        20. Rxg4 Rxd4 21. Be4 Bxe4 22. Qxe4 Rxe4 23. Kf2 f6 24. Rd1 Ra4 25. Rd7 1-0""",
        "Nimzo-Indian Defense",
        "1-0",
        2008,
        "World Championship Match"
    )
]