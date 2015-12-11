package com.kata
/**
 * Created by developer on 11/12/2015.
 */

object MorseCodeDecoder {

  sealed trait Tree[A] {
    def value: A
    def left: Option[Tree[A]]
    def right: Option[Tree[A]]
  }

  case class TreeNode (value:Char, left: Option[TreeNode], right: Option[TreeNode]) extends Tree[Char] {
  }

  def navigateByMorseChar(node: TreeNode, morseChar:Char) = morseChar match {
          case '.' => node.left
          case '-' => node.right
  }

  def decode(morseCode: String) : String = {
    val root = TreeNode('\0', Some(TreeNode('E', None, None)), Some(TreeNode('T', None, None)))

    val char = morseCode(0)
    val nextSeq = morseCode.substring(1)
    val node = navigateByMorseChar(root, char)
    node.get.value.toString
  }
}
