// https://code.google.com/codejam/contest/4384486/dashboard#s=p1
"""Pari is a powerful fairy who is fighting to protect Fairyland from evil witches. The witches are becoming more powerful every day, so Pari must use magical sticks to cast a protection spell. She can do this by arranging the sticks to form a convex polygon with non-zero area.

However, Pari cannot necessarily use whichever sticks she wants! All of the available sticks in Fairyland are packed together, forming a graph in which the edges are sticks and the nodes are endpoints of one or more sticks. (The sticks never touch each other except at endpoints; they are magical!) Whenever Pari removes a stick to use in her spell, all sticks that were adjacent to that stick (that is, that shared a node with that stick) disappear forever and cannot be used in the future.

Pari is wondering how many distinct subsets of sticks can be removed from the graph and used to form a convex polygon with nonzero area. All of the sticks are considered distinct, even sticks that have the same length. Two subsets of sticks are distinct if and only if there is at least one stick that is present in one subset but not the other. As stated above, a subset is only valid if there is a way to remove all of the sticks in that subset from the graph without any of them disappearing."""

// find all solutions
let solveByBacktracking (moves: 'a -> 'a seq) (solved: 'a -> bool) (initialState: 'a) :'a seq = 
    let rec inner (state: 'a) : 'a seq = 
        if state |> solved then
            state |> Seq.singleton
        else
            state |> moves |> Seq.collect inner
    initialState |> inner

type Stick = {length: int; endpoints: int * int}
let length stick = stick.length
let independent (stick1:Stick) (stick2:Stick) = 
    fst stick1.endpoints <> fst stick2.endpoints && fst stick1.endpoints <> snd stick2.endpoints && snd stick1.endpoints <> fst stick2.endpoints && snd stick1.endpoints <> snd stick2.endpoints

type PartialSolution = {picked: Stick list; remaining: Stick list} 

let T = System.Console.ReadLine() |> int
for case in [1..T] do
    let N = System.Console.ReadLine() |> int
    let L = Array2D.zeroCreate N N
    for i in [0..N-1] do
        L.[i,*] <- System.Console.ReadLine().Split() |> Array.map int

    let sticks = [for i in [0..N-1] do for j in [0..N-1] do if i < j && L.[i,j] > 0 then yield {length = L.[i,j]; endpoints = i,j }] |> List.sortByDescending length

    let solved solution =
        solution.remaining |> List.isEmpty && 
        let sticks = solution.picked
        let n = sticks |> List.length
        n >= 3 && (sticks |> List.map length |> List.max)*2 < (List.sumBy length sticks)

    let moves solution = 
        match solution.remaining with
        | stick::others ->
            seq {
                for included in [true; false] do
                if included then
                    yield {picked = stick::solution.picked; remaining = others |> List.where (independent stick) }
                else
                    yield {solution with remaining = others} }
        | _ -> Seq.empty

    let solution = {picked = []; remaining = sticks} |> solveByBacktracking moves solved |> Seq.length
    printfn "Case #%d: %d" case solution
