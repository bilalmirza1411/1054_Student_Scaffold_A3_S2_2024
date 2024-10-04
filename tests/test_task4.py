from __future__ import annotations

from typing import List
from unittest import TestCase

from config import Directions
from ed_utils.decorators import number, visibility
from maze import Maze, Position


"""
For FIT1054 STUDENTS ONLY
"""


class TestTask4(TestCase):
    @staticmethod
    def reset_visited_maze(maze: Maze) -> None:
        for row in maze.grid:
            for cell in row:
                cell.visited = False

    def validate_path(self, maze: Maze, path: List[Position]) -> bool:
        def valid_step(step: Position) -> bool:
            return maze.is_valid_position(step)
        self.reset_visited_maze(maze)

        # Check final position is an exit
        fp: Position = path[len(path) - 1]  # Final position
        self.assertTrue(fp in maze.end_positions, f"Expected the final position to be an exit got {fp} ({maze.grid[fp.row][fp.col]})")

        # Check initial position is a start
        self.assertEqual(path[0], maze.start_position, f"Expected the initial position to be the start position got {path[0]}, instead of {maze.start_position}")

        # check if all steps are valid
        valid_steps: List[bool] = list(map(valid_step, path))
        self.assertTrue(all(valid_steps), f"Invalid steps found in the path {path}")

        for step_num, step in enumerate(path):
            # check if the step is a valid move
            if step_num == len(path) - 1:
                continue
            next_step: Position = path[step_num + 1]

            # Check if we can move to the next step
            for direction in Directions:
                next_position: Position = Position(step.row + Maze.directions[direction][0], step.col + Maze.directions[direction][1])
                if next_position == next_step:
                    break
            else:
                self.fail(f"Invalid move from {step} to {next_step}")

    @number("4.1")
    @visibility(visibility.VISIBILITY_HIDDEN)
    def test_obvious_exit(self) -> None:
        maze: Maze = Maze.load_maze_from_file("/task4/maze1.txt")
        student_result: List[Position] = maze.quick_escape(40)
        self.assertIsNotNone(student_result, "Expected a path to be returned")
        self.validate_path(maze, student_result)
        self.assertEqual(len(student_result), 2, "Expected the path to be of length 2 (the exit is right next to the start)")

    @number("4.2")
    @visibility(visibility.VISIBILITY_HIDDEN)
    def test_exit_too_far(self) -> None:
        maze: Maze = Maze.load_maze_from_file("/task4/maze2.txt")
        student_result: List[Position] = maze.quick_escape(3)
        self.assertIsNone(student_result, "Expected no path to be found as the exit is too far")
        maze: Maze = Maze.load_maze_from_file("/task4/maze2.txt")
        student_result: List[Position] = maze.quick_escape(7)
        self.assertIsNotNone(student_result, "Expected a path to be returned")
        self.validate_path(maze, student_result)
        # Move right 7 times
        self.assertEqual(len(student_result), 8, "Expected the path to be of length")

    @number("4.3")
    @visibility(visibility.VISIBILITY_HIDDEN)
    def test_exit_just_close_enough(self) -> None:
        maze: Maze = Maze.load_maze_from_file("/task4/maze3.txt")
        student_result: List[Position] = maze.quick_escape(10)
        self.assertIsNotNone(student_result, "Expected a path out of the maze but no path out of the maze was found.")
        self.validate_path(maze, student_result)
        self.assertEqual(len(student_result), 11, "The shortest path is to move right 7 times then up 4 times")
        maze: Maze = Maze.load_maze_from_file("/task4/maze3.txt")
        self.assertIsNone(maze.quick_escape(9), "Expected no path to be found as there isn't enough stamina")

    @number("4.4")
    @visibility(visibility.VISIBILITY_HIDDEN)
    def test_bigger_maze(self) -> None:
        maze: Maze = Maze.load_maze_from_file("/task4/maze4.txt")
        student_result: List[Position] = maze.quick_escape(17)
        self.assertIsNotNone(student_result, "Expected a path out of the maze but no path out of the maze was found.")
        self.validate_path(maze, student_result)
        self.assertEqual(len(student_result), 18, "Shortest path is 18 steps including the start and end positions")
        maze: Maze = Maze.load_maze_from_file("/task4/maze4.txt")
        self.assertIsNotNone(maze.quick_escape(9000), "Expected a path out of the maze but no path out of the maze was found.")
        self.assertEqual(len(student_result), 18, "Shortest path is 18 steps including the start and end positions")
        self.validate_path(maze, student_result)
